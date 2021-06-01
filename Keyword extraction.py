from rake_nltk import Rake
rake_nltk_var = Rake()

text = """ T am a entrepreneur from Bangladesh, and I am learning about machine learning, data science, python, robotics, rpa and try to share my learnings. I hope you will learn a lot and that will  help me to enrich my knowledge."""

rake_nltk_var.extract_keywords_from_text(text)
keyword_extracted = rake_nltk_var.get_ranked_phrases()
print(keyword_extracted)
