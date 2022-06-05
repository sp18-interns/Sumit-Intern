from datetime import date

letter = '''Dear <|Name|>

You Have Sucessfull Passed the AZ-303
Your are now Azure Architect 

Date <|Date|>
This is to Certify that <|Name|> has cleared Microsoft Architect AZ-303 Exam


                                                            Microsoft CEO
                                                            SATYA NADELA
'''
name = input ("Enter your Name: ")
today = date.today()
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", str(today))
print(letter)
print(letter, file=open("%s.txt" %name, 'x'))