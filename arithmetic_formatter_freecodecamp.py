#Some variables are in French, others in English — I know it's not ideal practice, but let's go with it this time
def verify_operators(problems):
    operators=len(list(filter(lambda problem : problem.find("*")!=-1 or problem.find("/")!=-1 , problems)))
    if operators :
        return True
    else :
        return False

def verify_char(problems):
    char_autorise = "0123456789+-"
    for problem in problems:
        for char in problem:
            if char_autorise.find(char)==-1:
                return True

    return False
    
def arithmetic_arranger(problems,display = False):
    #regarder le nombre d'éléments de la liste
    if len(problems)>5 :
        return 'Error: Too many problems.'

    #formater le problème
    translation = str.maketrans({" ":""})
    problems=[problem.translate(translation) for problem in problems]

    #verifier les operateurs
    if verify_operators(problems):
        return "Error: Operator must be '+' or '-'."

    #verifier les caractères
    if verify_char(problems):
        return 'Error: Numbers must only contain digits.'

    _=[]
    #verifier le nombre de chiffres
    for problem in problems :
        if problem.find("+")!=-1:
            _.append([problem[0:problem.find("+")] ,problem[problem.find("+")+1::],"+"])
        else:
            _.append([problem[0:problem.find("-")] ,problem[problem.find("-")+1::],"-"])
    
    problems = _

    for problem in problems :
        if len(problem[0])>=5 or len(problem[1])>=5 :
            return 'Error: Numbers cannot be more than four digits.'

    #solution
    results = [ str(int(problem[0])+int(problem[1])) if problem[2]=="+" else str(int(problem[0])-int(problem[1])) for problem in problems]

    solution=""

    numero_ligne = 0
    
    while numero_ligne < 4 :
        counter = 0
        if numero_ligne == 0 :
            for problem in problems:
                max_digit = max(len(problem[0]),len(problem[1])) 
                solution+=" "*(max_digit-len(problem[0])+2)
                solution+=problem[0]
                if counter!=(len(problems)-1):
                    solution+=" "*4
                else:
                    solution+="\n"
                counter+=1

        elif numero_ligne == 1:
            for problem in problems:
                max_digit = max(len(problem[0]),len(problem[1])) 
                solution+=problem[2]+" "*(max_digit-len(problem[1])+1)
                solution+=problem[1]
                if counter!=(len(problems)-1):
                    solution+=" "*4
                else:
                    solution+="\n"
                counter+=1

        elif numero_ligne == 2:
            for problem in problems:
                max_digit = max(len(problem[0]),len(problem[1])) 
                solution+="-"*(max_digit+2)
                if counter!=(len(problems)-1):
                    solution+=" "*4

                counter+=1

        else :
            if display :
                solution+="\n"
                for problem in problems:
                    max_digit = max(len(problem[0]),len(problem[1])) 
                    solution+=" "*(2-abs(len(results[counter])-max_digit))
                    if display :
                        solution+=results[counter]
                        if display :
                            if counter!=(len(problems)-1):
                                 solution+=" "*4
                            else:
                                return solution
                            
                        counter+=1
            else:
                return solution
                
        numero_ligne += 1

    



