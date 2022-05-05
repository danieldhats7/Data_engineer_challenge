import requests
import json
import pandas as pd
from datetime import datetime


class Stackoverflow_questions:
    def __init__(self, URL):
        self.URL = URL
        self.resp_json = json.loads(requests.get(self.URL).text)
        self.df = pd.DataFrame(self.resp_json["items"])
        # Mejoranddo el formato de las fechas
        self.df["creation_date"] = self.df["creation_date"].apply(
            lambda x: datetime.fromtimestamp(x)
        )
        self.df["last_activity_date"] = self.df["last_activity_date"].apply(
            lambda x: datetime.fromtimestamp(x)
        )
        self.df["closed_date"] = self.df["closed_date"].apply(
            lambda x: datetime.fromtimestamp(x) if not pd.isna(x) else None
        )
        self.df["protected_date"] = self.df["protected_date"].apply(
            lambda x: datetime.fromtimestamp(x) if not pd.isna(x) else None
        )

    def answered_count(self) -> list:
        """
        returns a list with the number of questions answered and
        the number of questions unanswered

        Returns:
            (int, int): [answered_count, unanswered_count]
        """

        answered_count = self.df[
            self.df["is_answered"] == True]["is_answered"].shape[0]
        unanswered_count = self.df[
            self.df["is_answered"] == False]["is_answered"].shape[0]

        return [answered_count, unanswered_count]

    def question_views_min(self) -> str:
        """
        returns the question with the minimum number of views

        Returns:
            str: question with the least number of views in json format
        """

        q_views_min = self.df[
            self.df["view_count"] == self.df["view_count"].min()
            ].to_json(orient='records')
        return json.loads(q_views_min)

    def question_old_current(self) -> str:
        """
        returns the question with the oldest creation date and the
        question with the currentest creation date in json format

        Returns:
            [old, current]: [oldest creation question, currentest creation question]
            in json format
        """
        old = self.df[
            self.df["creation_date"] == self.df["creation_date"].min()
            ].to_json(orient='records')
        current = self.df[
            self.df["creation_date"] == self.df["creation_date"].max()
            ].to_json(orient='records')
        return [json.loads(old), json.loads(current)]

    def question_owner_highest_reputation(self) -> str:
        """
        returns the question with the highest reputation of the owner

        Returns:
            str: question with the highest reputation of the owner in json format
        """

        def aux(row):
            try:
                return row["reputation"]
            except KeyError:
                return 0

        df_1 = self.df.copy()
        df_1["owner_reputation"] = df_1["owner"].apply(aux)
        q_owner_highest_reputation = df_1[
            df_1["owner_reputation"] == df_1["owner_reputation"].max()
            ].to_json(orient='records')
        return json.loads(q_owner_highest_reputation)
