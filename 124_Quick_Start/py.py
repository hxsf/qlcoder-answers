d = [
    "    ",
    "=============<<<<<<<< Python Code >>>>>>>>=============",
    "d = [",
    "]",
    "for i in d[12:16]:",
    "    print i",
    "for i in d[:-1]:",
    "    print '%s%s%s%s%s%s,'%(d[0],d[0],d[0],chr(34),i,chr(34))",
    "print '%s%s%s%s%s'%(d[0],d[0],d[0],chr(34),chr(34))",
    "for i in d[16:23]:",
    "    print i",
    "=============<<<<<<<< Scala Code >>>>>>>>==========",
    "object Main {",
    "    def main(args: Array[String]): Unit = {",
    "        val q: Char = 34",
    "        val l: Array[String] = Array(",
    "        )",
    "        var i: Int = 0",
    "        for (i <- 24 to 27) {println(l(i))}",
    "        for (j <- 0 until l.length) println(l(0) + l(0) + l(0) + q + l(j) + q + ',')",
    "        for (i <- 28 until l.length) {println(l(i))}",
    "    }",
    "}",
    "=============<<<<<<<< Java Code >>>>>>>>==========",
    "public class Main {",
    "    public static void main(String[] args) {",
    "        char q = 34;",
    "        String[] l = {",
    "        };",
    "        for(int i = 2; i <= 2; i++)",
    "            System.out.println(l[i]);",
    "        for(int i = 0; i < l.length; i++)",
    "            System.out.println(l[0] + q + l[i] + q + ',');",
    "        for(int i = 3; i <= 10; i++)",
    "            System.out.println(l[i]);",
    "    }",
    "}",
    "",
]
for i in d[12:16]:
    print i
for i in d[:-1]:
    print '%s%s%s%s%s%s,'%(d[0],d[0],d[0],chr(34),i,chr(34))
print '%s%s%s%s%s'%(d[0],d[0],d[0],chr(34),chr(34))
for i in d[16:23]:
    print i
