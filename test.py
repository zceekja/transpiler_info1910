import transpiler
import unittest
import sys
import subprocess


class Tests(unittest.TestCase):
    def test_add1(self):
        subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-add1.c", "tests/py-files/test-add1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-add1.py"])
        f = open("tests/expected/add1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_add2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-add2.c", "tests/py-files/test-add2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-add2.py"])
        f = open("tests/expected/add2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_mul1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-mul1.c", "tests/py-files/test-mul1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-mul1.py"])
        f = open("tests/expected/mul1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_mul2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-mul2.c", "tests/py-files/test-mul2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-mul2.py"])
        f = open("tests/expected/mul2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_struct1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-struct1.c", "tests/py-files/test-struct1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-struct1.py"])
        f = open("tests/expected/struct1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_struct2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-struct2.c", "tests/py-files/test-struct2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-struct2.py"])
        f = open("tests/expected/struct2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_ifelse1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-ifelse1.c", "tests/py-files/test-ifelse1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-ifelse1.py"])
        f = open("tests/expected/ifelse1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_ifelse2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-ifelse2.c", "tests/py-files/test-ifelse2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-ifelse2.py"])
        f = open("tests/expected/ifelse2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_cmdarg1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-cmdarg1.c", "tests/py-files/test-cmdarg1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-cmdarg1.py", "Hello"])
        f = open("tests/expected/cmdarg1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_cmdarg2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-cmdarg2.c", "tests/py-files/test-cmdarg2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-cmdarg2.py", "Kittibhumi","Jaggabatara"])
        f = open("tests/expected/cmdarg2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_while1(self):
        subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-while1.c", "tests/py-files/test-while1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-while1.py"])
        f = open("tests/expected/while1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_while2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-while2.c", "tests/py-files/test-while2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-while2.py"])
        f = open("tests/expected/while2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_for1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-for1.c", "tests/py-files/test-for1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-for1.py"])
        f = open("tests/expected/for1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_for2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-for2.c", "tests/py-files/test-for2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-for2.py"])
        f = open("tests/expected/for2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_do1(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-do1.c", "tests/py-files/test-do1.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-do1.py"])
        f = open("tests/expected/do1.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

    def test_do2(self):
        output = subprocess.run(
            ["python3", "transpiler.py", "tests/c-files/test-do2.c", "tests/py-files/test-do2.py"])
        output = subprocess.check_output(
            ["python3", "tests/py-files/test-do2.py"])
        f = open("tests/expected/do2.txt")
        expected = f.read()
        self.assertEqual(output.decode('ascii'), expected)
        f.close()

if __name__ == '__main__':
    unittest.main()
