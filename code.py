# fun_placeholder.py

def fibonacci_sequence(n):
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

def pi_digits(n):
    # Spigot algorithm for digits of pi (simplified for small n)
    q, r, t, k, n_, l = 1, 0, 1, 1, 3, 3
    result = []
    for _ in range(n):
        if 4*q + r - t < n_ * t:
            result.append(n_)
            q, r, t, n_, l = (
                10*q,
                10*(r - n_ * t),
                t,
                (10*(3*q + r)) // t - 10*n_,
                l,
            )
        else:
            q, r, t, n_, l = (
                q * k,
                (2*q + r)*l,
                t * l,
                (q * (7*k + 2) + r * l) // (t * l),
                l + 2,
            )
            k += 1
    return result

def main():
    n = 10  # You can increase this for more digits/terms
    print("First", n, "digits of π:")
    print("3." + ''.join(map(str, pi_digits(n)[1:])))
    
    print("\nFirst", n, "Fibonacci numbers:")
    print(fibonacci_sequence(n))

if __name__ == "__main__":
    main()
