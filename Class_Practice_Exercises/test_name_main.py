# 1 before python runs any code it sets special variables,
# directly it sets __name__ to main.

if __name__ == "__main":
    print(f'Original file: {__name__}')
else:
    print(f'Not in main')