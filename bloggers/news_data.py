class NewsData:
    def __init__(self):
        self.news = [
            {"title": "MrBeast запускає новий челлендж", "source": "YouTube", "link": "https://www.youtube.com/user/MrBeast6000"},
            {"title": "PewDiePie випустив нове відео про ігри", "source": "YouTube", "link": "https://www.youtube.com/user/PewDiePie"},
            {"title": "Emma Chamberlain поділилася лайфстайл порадами", "source": "Instagram", "link": "https://www.instagram.com/emmachamberlain/"},
            {"title": "James Charles анонсував нову косметичну лінію", "source": "YouTube", "link": "https://www.youtube.com/user/jamescharles"}
        ]

    def get_all_news(self):
        return self.news

