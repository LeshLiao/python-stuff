


'''
parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
returns: ["fr-FR", "fr-CA"]
'''

def is_valid(matched_languages, fir):
  for item in matched_languages:
    if fir == item:
      return False
  return True


def parse_accept_language(application_language, firmware_supported_languages):
  application_list = application_language.split(", ")
  matched_languages = []
  for lan in application_list:
    for fir in firmware_supported_languages:
      if lan == fir or lan in fir[:2]:
        if is_valid(matched_languages, fir):
          matched_languages.append(fir)


  print(matched_languages)
  return matched_languages



def run_all_tests():

  #question 1
  application_language = "en-US, fr-CA, fr-FR"
  firmware_supported_languages = ["fr-FR", "en-US"]
  expected = ["en-US", "fr-FR"]
  result = parse_accept_language(application_language, firmware_supported_languages)

  assert result == expected
  print("1. passed!")

  # question 2
  assert parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]) == ["fr-FR"]
  print("2. passed!")

  # question 3
  assert parse_accept_language("en-US", ["en-US", "fr-CA"]) == ["en-US"]
  print("3. passed!")

  # question 4
  parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]) == ["en-US"]
  assert parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]) == ["en-US"]
  print("4. passed!")

  # question 5
  assert parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"]) == ["fr-CA", "fr-FR"]
  print("5. passed!")

  # question 6
  assert parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"]) == ["fr-FR", "fr-CA"]
  print("6. passed!")

run_all_tests()
