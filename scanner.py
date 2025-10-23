Keyword={ 'int' ,'float' ,'return' ,'if' ,'else' ,'for' ,'while' ,'do' ,'break' ,'continue' ,'switch',
          'case' ,'default' ,'char' ,'double' ,'long' ,'short' ,'void' ,'static'       }

Operators={ '+' ,'-' ,'*' ,'/' ,'%' ,'=' ,'>' ,'<' ,'!' ,'&' ,'|' }

Special_Characters={';' ,'{' ,'}' ,'(' ,')' ,'[' ,']' ,'!' ,'&' ,'|'}

space={ " " ,"\t" ,"\n"}

def scanner(input_code):
  result_tokens=[]
  curr_token=""

  for char in input_code:
    if char in space:
      if len(curr_token)>0:
        if curr_token in Keyword:
                    result_tokens.append((curr_token ,"Keyword"))
        elif curr_token.isdigit():
            result_tokens.append((curr_token ,"Number"))
        else:
            result_tokens.append((curr_token ,"Identifier"))
        curr_token = ""
    elif char in Special_Characters:
      if len(curr_token)>0:
        if curr_token in Keyword:
            result_tokens.append((curr_token ,"Keyword"))
        elif curr_token.isdigit():
            result_tokens.append((curr_token ,"Number"))
        else:
            result_tokens.append((curr_token ,"Identifier"))
        curr_token = ""
      result_tokens.append((char ,"Special Character"))
    elif char in Operators:
      if len(curr_token)>0:
        if curr_token in Keyword:
                    result_tokens.append((curr_token ,"Keyword"))
        elif curr_token.isdigit():
            result_tokens.append((curr_token ,"Number"))
        else:
            result_tokens.append((curr_token ,"Identifier"))
        curr_token = ""
      result_tokens.append((char ,"Operator"))

    else:
      curr_token += char

  if curr_token:
        if curr_token in Keyword:
            result_tokens.append((curr_token ,"Keyword"))
        elif curr_token.isdigit():
            result_tokens.append((curr_token ,"Number"))
        else:
            result_tokens.append((curr_token ,"Identifier"))

  return result_tokens


input_code=input("Enter a code in C: ")
output=scanner(input_code)
for i,j in output:
  print(f"{i}: {j}")