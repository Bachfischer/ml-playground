def main():

    # TBD
    input = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]

    query = "ball"

    index = 0
    for key in input:
        if key == query:
            print("Found query key at index position ", index)
            break
        index +=1

if __name__ == "__main__":
    main()