import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Random;

public class HomomorphismRSA {

    private static final int Iteration = 10; // Number of tests
    private static final int MaxRandomVal = 1000;

    public static void main(String[] args) {

        Random random = new Random();

        for (int i = 1; i <= Iteration; i++) {
            System.out.println("Iteration =  " + i);

            RSA rsa = new RSA(); // Generate keys

            BigInteger Number1 = new BigInteger(String.valueOf(random.nextInt(MaxRandomVal))); // Create integer number 1
            BigInteger Number2 = new BigInteger(String.valueOf(random.nextInt(MaxRandomVal))); // Create integer number 2

            System.out.println(String.format("Random numbers are Number1=%s, Number2=%s", Number1, Number2));

            BigInteger numFinal = Number1.multiply(Number2); // Multiplying the two numbers

            System.out.println(String.format("Multiplication result of numbers: %s", numFinal));

            BigInteger encNumber1 = rsa.Encrypt(Number1); // Encrypt number one
            BigInteger encNumber2 = rsa.Encrypt(Number2); // Encrypt number two

            BigInteger encFinal = encNumber1.multiply(encNumber2).mod(rsa.getN()); // Encrypted numbers - Multiply and mod n

            System.out.println(String.format("Encrypted Values =\n Number1=%s\n Number2=%s", encNumber1, encNumber2));
            System.out.println(String.format("Multiplication of Encrypted numbers=\n %s", encFinal));

            BigInteger decFinal = rsa.Decrypt(encFinal); // Multiplied encrypted numbers are decrypted
            System.out.println(String.format("Multiplied encrypted numbers are decrypted = %s", decFinal));

            System.out.println(String.format("Homomorphic = %s\n\n", numFinal.equals(decFinal) ? "YES" : "NO"));
        }
    }

    // Simple RSA implementation with BigInteger
    static class RSA {

        private BigInteger e;
        private BigInteger n;
        private BigInteger d;

        public RSA() {

            final int BitLen = 1024;

            // Generating random prime numbers
            Random rand = new SecureRandom();
            BigInteger p = BigInteger.probablePrime(BitLen / 2, rand);
            BigInteger q = BigInteger.probablePrime(BitLen / 2, rand);

            // Calculate products
            n = p.multiply(q);
            BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract(BigInteger.ONE));

            // Generating public key and private key
            e = BigInteger.valueOf(65537); // Common choice for e
            d = e.modInverse(phi);
        }

        public BigInteger Encrypt(BigInteger plainText) { // Encryption function
            return plainText.modPow(e, n);
        }

        public BigInteger Decrypt(BigInteger cipher) { // Decryption function
            return cipher.modPow(d, n);
        }

        public BigInteger getN() {
            return n;
        }
    }
}
