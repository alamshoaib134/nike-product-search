# Contributing to Nike Product Search Application

Thank you for your interest in contributing to our project! Here's how you can help:

## Getting Started

1. Fork the repository
2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Copy `src/config_sample.py` to `src/config_local.py` and add your credentials
4. Create required directories:
```bash
mkdir -p product_images test_images
```

## Development Process

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes, ensuring you:
   - Follow existing code style
   - Add appropriate tests
   - Update documentation as needed
   - Remove any sensitive information
   - Keep commits focused and meaningful

3. Test your changes:
   - Run all tests: `python -m pytest tests/`
   - Test with sample data
   - Verify no sensitive information is included

4. Submit a Pull Request:
   - Provide clear description of changes
   - Reference any related issues
   - Include screenshots for UI changes
   - List any new dependencies added

## Code Style Guidelines

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and concise
- Comment complex logic
- Use type hints where appropriate

## Testing Guidelines

- Write unit tests for new features
- Include edge cases and error conditions
- Mock external services (e.g., Google Images API)
- Maintain test coverage
- Use descriptive test names

## Documentation

Update documentation when you:
- Add new features
- Change existing functionality
- Modify configuration options
- Add new dependencies

## Questions or Problems?

- Check existing issues first
- Open new issue with clear description
- Include relevant code snippets
- Provide steps to reproduce problems

## License

By contributing, you agree that your contributions will be licensed under the MIT License.