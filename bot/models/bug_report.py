from datetime import datetime

class BugReport:
    def __init__(self, category: str, description: str):
        self.category = category
        self.description = description
        self.created_at = datetime.now()

    def __repr__(self):
        return f"BugReport(category={self.category}, description={self.description}, created_at={self.created_at})"
