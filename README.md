# 🎲 Guess the Number

A fun and interactive number‑guessing game deployed on the Algorand blockchain 🛸

---

## 🚀 Table of Contents

| Section | Description |
|--------|-------------|
| [About](#-about) | What the project is about |
| [Features](#-features) | Core capabilities |
| [Tech Stack](#-tech-stack) | Technologies & tools used |
| [Getting Started](#-getting-started) | Installation & running |
| [Usage](#-usage) | How to play the game |
| [License](#-license) | Licensing information |
| [Author & Links](#-author--links) | Contact info |

---

## ✨ About

**"Guess the Number"** is a simple yet engaging game built on the **Algorand blockchain**. A smart contract (written in **AlgoPy**) generates a secret number, and users try to guess it via a sleek **React** frontend. The contract then responds with `"Correct!"` or `"Wrong!"` depending on the guess.

Perfect as a demo for smart-contract interaction, web3 gaming principles, and Algorand-based development.

---

## 🔍 Features

- ✅ Blockchain-backed number guessing logic  
- 🎭 Smart contract written in AlgoPy  
- 🧩 Interactive web-based interface using React  
- 🛡️ Decentralized and trustless gameplay  

---

## 💻 Tech Stack

```md
- **Smart Contract**: AlgoPy (Python for Algorand)
- **Frontend**: React.js (with HTML, CSS)
- **Blockchain**: Algorand Testnet/Mainnet
- **Package Manager**: npm or yarn
```

---


## 🧭 Getting Started

Follow along to get the game running locally:

1. **Clone the repo**
    ```bash
    git clone https://github.com/kranthi1306/guess_number
    cd guess-the-number
    ```

2. **Install dependencies**
    ```bash
    cd frontend
    npm install
    ```

3. **Deploy the smart contract**
    ```bash
    cd ../scripts
    python3 deploy_contract.py
    ```
   > ⚠️ Make sure you have access to an Algorand node or use AlgoNode/AlgoSigner with funds on Testnet/Mainnet.

4. **Run the React frontend**
    ```bash
    cd ../frontend
    npm start
    ```
   The app will be available at `http://localhost:3000`.

---

## 🎮 Usage

1. Open the frontend.
2. Enter your guess (e.g. a number between 1–100).
3. Click “Submit.”
4. Read the response from the blockchain: “Correct!” or “Wrong, try again.”

Repeat until you find the secret number!

---

## 🛡️ License

Released under the **MIT License** – see [`LICENSE`](LICENSE) for details.

---

## 👤 Author & Links

**Kranthi Priya Maganti**  
- 💼 [LinkedIn](https://www.linkedin.com/in/kranthi-maganti-505265351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
- 🐦 [Twitter](https://x.com/kra95682?s=08)  
  
