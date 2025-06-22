from S1E9 import Character, Stark


def main():
    try:
        # Creating Ned Stark
        Ned = Stark("Ned")
        print(Ned.__dict__)  # Print internal attributes
        print(Ned.is_alive)  # Should be True
        Ned.die()  # Ned dies
        print(Ned.is_alive)  # Should be False
        print(Ned.__doc__)  # Class docstring
        print(Ned.__init__.__doc__)  # Constructor docstring
        print(Ned.die.__doc__)  # Method docstring
        print("---")

        # Creating Lyanna Stark who is already dead
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)  # Should show is_alive as False

        # Should raise an error: Can't instantiate abstract class
        hodor = Character("Hodor")
        print(hodor)

    except TypeError as e:
        print("TypeError:", e)
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
