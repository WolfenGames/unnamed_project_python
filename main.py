from Sandbox.src.Sanbox import CreateApplication

if __name__ == "__main__":
    try:
        sb = CreateApplication()
        sb.Run()
    except KeyboardInterrupt:
        print(f"Ungracefully demise")
