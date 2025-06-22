def generate_code(prompt):
    prompt = prompt.lower().strip()

    if "factorial" in prompt and "python" in prompt:
        return '''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
'''
    elif "fibonacci" in prompt and "python" in prompt:
        return '''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
'''
    elif "prime" in prompt and "python" in prompt:
        return '''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
'''
    elif "prime" in prompt and "java" in prompt:
        return '''import java.util.Scanner;

public class PrimeCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check: ");
        int num = sc.nextInt();
        sc.close();

        if (isPrime(num)) {
            System.out.println(num + " is a Prime number.");
        } else {
            System.out.println(num + " is NOT a Prime number.");
        }
    }

    public static boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
'''
    elif "fibonacci" in prompt and "java" in prompt:
        return '''import java.util.Scanner;

public class FibonacciLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of terms: ");
        int n = sc.nextInt();
        sc.close();

        int first = 0, second = 1;

        System.out.println("Fibonacci Series up to " + n + " terms:");
        for (int i = 1; i <= n; i++) {
            System.out.print(first + " ");
            int next = first + second;
            first = second;
            second = next;
        }
    }
}
'''
    elif "factorial" in prompt and "java" in prompt:
        return '''import java.util.Scanner;

public class FactorialLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        sc.close();

        long factorial = 1;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }

        System.out.println("Factorial of " + n + " is: " + factorial);
    }
}
'''
    elif "help" in prompt or prompt == "":
        return '''
Available Code Options:
- Find factorial number in Python
- Find fibonacci number in Python
- Find prime number in Python
- Find factorial number in Java
- Find fibonacci number in Java
- Find prime number in Java
Type your request like: "Find factorial in python"
'''
    else:
        return "# ❗ Sorry, I don’t recognize that request.\n# ➔ Type 'help' to see available options."


# Program loop
print("=== Code Generator ===")
print("Type 'help' for options or 'exit' to quit.")
while True:
    user_prompt = input("\nDescribe what code you want: ")
    if user_prompt.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
    print("\nGenerated Code:\n")
    print(generate_code(user_prompt))
