
def show_intervals():
    while True:
        try:
            x, y = map(int, input().split())
        except EOFError:
            print("No input provided")
            break
        except TypeError:
            print("Incorrect type")
            break
        except ValueError:
            print("invalid interval")
            break
        else:
                if x<=y:
                    for z in range(x, y+1):
                      print(z, end=" ") 
                    print("\n")
                    break
                else:   
                    print("invalid interval")
        
        

def main():
    show_intervals()

if __name__== "__main__" :
    main()
    