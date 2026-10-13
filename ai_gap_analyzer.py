```python
class SkillGapAnalyzer:
    def __init__(self):
        self.jobs = {
            "python developer": {"python", "sql", "git", "django"},
            "data analyst": {"python", "sql", "excel", "power bi"},
            "web developer": {"html", "css", "javascript", "python"}
        }

    def analyze(self, role, skills):
        role = role.lower().strip()

        if role not in self.jobs:
            print("Career role not available!")
            return

        required = self.jobs[role]
        existing = {s.strip().lower() for s in skills.split(",") if s.strip()}

        matched = required & existing
        missing = required - existing
        score = len(matched) / len(required) * 100

        print("\nAI GAP ANALYZER")
        print("Career:", role.title())
        print("Matched Skills:", sorted(matched))
        print("Missing Skills:", sorted(missing))
        print("Career Readiness:", round(score, 2), "%")

        print("\nLearning Roadmap:")
        for skill in sorted(missing):
            print("- Learn", skill)


analyzer = SkillGapAnalyzer()

role = input("Enter career (Python Developer/Data Analyst/Web Developer): ")
skills = input("Enter your skills separated by commas: ")

analyzer.analyze(role, skills)
```
