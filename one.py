import sign_language_translator as slt
# print(slt.TextLanguageCodes, slt.SignLanguageCodes)

# The core model of the project (rule-based text-to-sign translator)
# which enables us to generate synthetic training datasets
model = slt.models.ConcatenativeSynthesis(
   text_language='eng', sign_language="pk-sl", sign_format="video"
)
slt.TextLanguageCodes.
text = 'Hi' # "This very good is."
sign = model.translate(text) # tokenize, map, download & concatenate
sign.show()
# sign.save(f"{text}.mp4")

model.text_language = "hindi"  # slt.TextLanguageCodes.HINDI  # slt.languages.text.Hindi()
sign_2 = model.translate("पाँच घंटे।") # "5 hours."