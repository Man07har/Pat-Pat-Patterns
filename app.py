import matplotlib.pyplot as plt





def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = naive_string_match(text, pattern)
print("Naive String Matching Algorithm:")
print(f"Pattern found at positions: {matches}")



# KMP Algorithm
def __run__kmp_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    lps = [0] * m  # Longest Prefix Suffix array

    # Preprocess the pattern to create the lps array
    __run__compute_lps(pattern, lps)

    i, j = 0, 0  # Text and Pattern indices
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

    return matches

def __run__compute_lps(pattern, lps):
    m = len(pattern)
    lps[0] = 0
    j = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

# Boyer-Moore Algorithm
def __run__boyer_moore_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Precompute the last occurrence function
    last = {}
    for i in range(m):
        last[pattern[i]] = i

    i = m - 1  # Text index
    k = m - 1  # Pattern index

    while i < n:
        j = k
        while j >= 0 and text[i - k + j] == pattern[j]:
            j -= 1

        if j < 0:
            matches.append(i - k)
            i += 1
        else:
            i += max(1, k - last.get(text[i], -1))

        k = m - 1

    return matches

# Z Algorithm
def __run__z_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Concatenate pattern and text for Z-algorithm
    concat = pattern + '$' + text
    z = [0] * len(concat)

    # Compute Z-array
    l, r = 0, 0
    for i in range(1, len(concat)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(concat) and concat[z[i]] == concat[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    # Find matches
    for i in range(m, n + m):
        if z[i] == m:
            matches.append(i - m - 1)

    return matches




def simulate_naive(text, pattern):   #_________________________________________________________________
    n = len(text)
    m = len(pattern)
    st.write(f"Text: {text}")
    st.write(f"Pattern: {pattern}")

    for i in range(n - m + 1):
        j = 0
        while j < m:
            st.write(f"Checking text from position {i} to {i + m}: {text[i:i + m]}")
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            st.write("Pattern found at position:", i)
            st.write("Pattern:", pattern)
            break
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation


def compute_lps(pattern):    #______________________________________________________________________
    m = len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def simulate_kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    st.write(f"Text: {text}")
    st.write(f"Pattern: {pattern}")
    i = j = 0
    while i < n:
        st.write(f"Checking text from position {i} to {i + m}: {text[i:i + m]}")
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            st.write("Pattern found at position:", i - j)
            st.write("Pattern:", pattern)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation


def simulate_boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    # Precompute the last occurrence function
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    
    # Initialize the shift amount
    k = m
    
    while k <= n:
        j = m - 1
        i = k - 1
        found = True
        
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        
        st.write(f"Checking text from position {i + 1} to {k}: {text[i + 1:k + 1]}")
        st.write(f"Pattern: {pattern}")
        
        if j < 0:
            st.write(f"Pattern found at index {i + 1}")
            k += m - last.get(text[i], -1)
        else:
            shift = max(1, j - last.get(text[i], -1))
            st.write(f"Mismatch at index {i + 1}, shifting by {shift}")
            k += shift
        
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation

def compute_z(text):   #_________________________________________________________________________________
    n = len(text)
    z = [0] * n
    l, r, k = 0, 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and text[z[i]] == text[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def simulate_z_algorithm(text, pattern):
    n = len(text)
    m = len(pattern)
    concat_str = pattern + "$" + text
    z = compute_z(concat_str)
    st.write(f"Text: {text}")
    st.write(f"Pattern: {pattern}")
    for i in range(n):
        if z[i + m + 1] == m:
            st.write("Pattern found at position:", i)
            st.write("Pattern:", pattern)
        st.write(f"Checking text from position {i} to {i + m}: {text[i:i + m]}")
        st.write(f"Z-value: {z[i + m + 1]}")
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation

def simulate_rabin_karp(text, pattern):      #__________________________________________________________________
    n = len(text)
    m = len(pattern)
    pattern_hash = sum(ord(pattern[i]) for i in range(m))

    st.write(f"Text: {text}")
    st.write(f"Pattern: {pattern}")

    for i in range(n - m + 1):
        current_text = text[i:i + m]
        current_hash = sum(ord(current_text[j]) for j in range(m))

        st.write(f"Checking text from position {i} to {i + m}: {current_text}")
        st.write(f"Text Hash: {current_hash}")

        if current_hash == pattern_hash and current_text == pattern:
            st.write("Pattern found at position:", i)
            st.write("Pattern:", pattern)
            break
        st.write("---")
        time.sleep(1)  # Sleep for 1 second to simulate the animation

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    # Calculate hash of the pattern
    pattern_hash = sum(ord(pattern[i]) for i in range(m))

    for i in range(n - m + 1):
        # Calculate hash of the current substring of text
        text_hash = sum(ord(text[i + j]) for j in range(m))
        if text_hash == pattern_hash and text[i:i + m] == pattern:
            matches.append(i)

    return matches

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = rabin_karp(text, pattern)
print("Rabin-Karp Algorithm:")
print(f"Pattern found at positions: {matches}")

import streamlit as st
import time

# Function to measure execution time
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

# Streamlit UI
st.title("String Matching Algorithms Comparison")

text = st.text_input("Enter text:")
pattern = st.text_input("Enter pattern:")

option = st.radio("Choose an option:", ["Run", "Simulation"])

if option == "Run":
    if st.button("Run"):
        st.write("Running Naive String Matching Algorithm...")
        naive_result, naive_time = measure_time(naive_string_match, text, pattern)
        st.write(f"Naive Algorithm Result: {naive_result}")
        st.write(f"Naive Algorithm Execution Time: {naive_time} seconds")

        st.write("Running Rabin-Karp Algorithm...")
        rabin_result, rabin_time = measure_time(rabin_karp, text, pattern)
        st.write(f"Rabin-Karp Algorithm Result: {rabin_result}")
        st.write(f"Rabin-Karp Algorithm Execution Time: {rabin_time} seconds")

        st.write("Running KMP Algorithm...")
        kmp_result, kmp_time = measure_time(__run__kmp_string_match, text, pattern)
        st.write(f"KMP Algorithm Result: {kmp_result}")
        st.write(f"KMP Algorithm Execution Time: {kmp_time} seconds")

    
        st.write("Running Z-Algorithm...")
        z_result, z_time = measure_time(__run__z_string_match, text, pattern)
        st.write(f"Z-Algorithm Result: {z_result}")
        st.write(f"Z-Algorithm Execution Time: {z_time} seconds")

        st.write("Running Boyer-Moore Algorithm...")
        bm_result, bm_time = measure_time(__run__boyer_moore_string_match, text, pattern)
        st.write(f"Boyer-Moore Algorithm Result: {bm_result}")
        st.write(f"Boyer-Moore Algorithm Execution Time: {bm_time} seconds")


        st.write("Algorithm Comparison:")
        results = [naive_result, rabin_result, kmp_result, bm_result, z_result]
        if all(result == results[0] for result in results):
            st.write("All algorithms found the same matches.")
        else:
            st.write("Algorithms produced different results.")

        algorithm_names = ['Naive', 'Rabin-Karp', 'KMP', 'Z-Algorithm', 'Boyer-Moore']
        execution_times = [naive_time, rabin_time, kmp_time, z_time, bm_time]

        fig, ax = plt.subplots()
        ax.bar(algorithm_names, execution_times)
        ax.set_xlabel('Algorithm')
        ax.set_ylabel('Execution Time (seconds)')
        ax.set_title('String Matching Algorithm Performance')

        # Display the bar chart in Streamlit
        st.pyplot(fig)




if option == "Simulation":
    Simulationoption = st.radio("Choose an Algorithm:", ["Naive", "KMP", "Boyer Moore", "Rabin Karp", "Z algorithm"])

    if Simulationoption == "Naive":
        st.title("Naive Algorithm Simulation")
        text = st.text_input("Enter text:", key=1)
        pattern = st.text_input("Enter pattern:", key=2)
        if st.button("Run Simulation"):
            st.write("Running Naive Algorithm Simulation...")
            simulate_naive(text, pattern)

    elif Simulationoption == "KMP":
        st.title("KMP Algorithm Simulation")
        text = st.text_input("Enter text:", key=3)
        pattern = st.text_input("Enter pattern:", key=4)
        if st.button("Run Simulation"):
            st.write("Running KMP Algorithm Simulation...")
            simulate_kmp(text, pattern)

    elif Simulationoption == "Boyer Moore":
        st.title("Boyer Moore Algorithm Simulation")
        text = st.text_input("Enter text:", key=5)
        pattern = st.text_input("Enter pattern:", key=6)
        if st.button("Run Simulation"):
            st.write("Running Boyer Moore Algorithm Simulation...")
            simulate_boyer_moore(text, pattern)

    elif Simulationoption == "Rabin Karp":
        st.title("Rabin-Karp Algorithm Simulation")
        text = st.text_input("Enter text:", key=7)
        pattern = st.text_input("Enter pattern:", key=8)
        if st.button("Run Simulation"):
            st.write("Running Rabin-Karp Algorithm Simulation...")
            simulate_rabin_karp(text, pattern)

    elif Simulationoption == "Z algorithm":
        st.title("Z Algorithm Simulation")
        text = st.text_input("Enter text:", key=9)
        pattern = st.text_input("Enter pattern:", key=10)
        if st.button("Run Simulation"):
            st.write("Running Z Algorithm Simulation...")
            simulate_z_algorithm(text, pattern)


