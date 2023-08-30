n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)

#adding main function
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)


if __name__ == "__main__":
    main()

# call sheep function
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()

# create flock
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()

# yeild generator
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
