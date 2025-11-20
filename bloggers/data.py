class BloggerData:
    def __init__(self):
        self.bloggers = [
            {"id": 1, "name": "MrBeast", "category": "Entertainment / Challenges",
             "description": "Відомий YouTube-блогер.", "social": {"YouTube": "https://www.youtube.com/user/MrBeast6000"}},
            {"id": 2, "name": "PewDiePie", "category": "Gaming / Entertainment",
             "description": "Популярний YouTube-блогер.", "social": {"YouTube": "https://www.youtube.com/user/PewDiePie"}},
            {"id": 3, "name": "Emma Chamberlain", "category": "Lifestyle / Vlogs",
             "description": "Американська блогерка.", "social": {"YouTube": "https://www.youtube.com/user/emmachamberlain"}},
            {"id": 4, "name": "James Charles", "category": "Beauty / Tutorials",
             "description": "Бьюті-блогер.", "social": {"YouTube": "https://www.youtube.com/user/jamescharles"}}
        ]

    def get_all_bloggers(self):
        return self.bloggers

    def get_blogger_by_id(self, blogger_id):
        for b in self.bloggers:
            if b["id"] == blogger_id:
                return b
        return None

