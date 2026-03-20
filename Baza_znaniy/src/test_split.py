from app.services.text_splitter import split_markdown_file


def main():
    file_path = "../../docs_parsing/test_opencode.md"
    print(f"Testing split on: {file_path}")
    try:
        result = split_markdown_file(file_path)
        print(f"Split result ({len(result)} parts):")
        for part in result:
            print(f" - {part}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
