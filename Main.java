package HumanClass;


// Parent class: Human
class Human {
    private String name;
    private String origin;

    // Constructor
    public Human(String name, String origin) {
        this.name = name;
        this.origin = origin;
    }

    // Method: eat
    public void eat() {
        System.out.println(name + " is enjoying a meal.");
    }

    // Method: sleep
    public void sleep() {
        System.out.println(name + " is getting some rest.");
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Getter for origin
    public String getOrigin() {
        return origin;
    }
}

// Subclass: Javanese, inheriting from Human
class Javanese extends Human {
    private String favoriteBatik;

    // Constructor
    public Javanese(String name, String origin, String favoriteBatik) {
        super(name, origin);
        this.favoriteBatik = favoriteBatik;
    }

    // Method override: eat
    @Override
    public void eat() {
        System.out.println(getName() + " is enjoying a delicious Gudeg, their favorite food.");
    }

    // Method: dance
    public void dance() {
        System.out.println(getName() + " is performing a graceful Javanese dance.");
    }

    // Getter for favoriteBatik
    public String getFavoriteBatik() {
        return favoriteBatik;
    }
}

// Subclass: Chinese, inheriting from Human
class Chinese extends Human {
    private String dialect;

    // Constructor
    public Chinese(String name, String origin, String dialect) {
        super(name, origin);
        this.dialect = dialect;
    }

    // Method override: eat
    @Override
    public void eat() {
        System.out.println(getName() + " is having dim sum for lunch.");
    }

    // Method: celebrateImlek
    public void celebrateImlek() {
        System.out.println(getName() + " is celebrating Imlek with family and friends.");
    }

    // Getter for dialect
    public String getDialect() {
        return dialect;
    }
}

// Subclass: Hakka, inheriting from Chinese
class Hakka extends Chinese {
    // Constructor
    public Hakka(String name, String origin, String dialect) {
        super(name, origin, dialect);
    }

    // Method: celebrateHakkaCuisine
    public void celebrateHakkaCuisine() {
        System.out.println(getName() + " is savoring authentic Hakka cuisine.");
    }

    // Method override: eat
    @Override
    public void eat() {
        System.out.println(getName() + " is having Hakka-style dishes for dinner.");
    }
}

// Subclass: Banyumasan, inheriting from Javanese
class Banyumasan extends Javanese {
    private String ngapakSkill;

    // Constructor
    public Banyumasan(String name, String origin, String favoriteBatik, String ngapakSkill) {
        super(name, origin, favoriteBatik);
        this.ngapakSkill = ngapakSkill;
    }

    // Method: speakNgapak
    public void speakNgapak() {
        System.out.println(getName() + " is speaking with a Banyumasan accent (Ngapak).");
    }

    // Getter for ngapakSkill
    public String getNgapakSkill() {
        return ngapakSkill;
    }
}

// Subclass: Surabayan, inheriting from Javanese
class Surabayan extends Javanese {
    private String favoriteDish;

    // Constructor
    public Surabayan(String name, String origin, String favoriteBatik, String favoriteDish) {
        super(name, origin, favoriteBatik);
        this.favoriteDish = favoriteDish;
    }

    // Method override: eat
    @Override
    public void eat() {
        System.out.println(getName() + " is enjoying a plate of " + favoriteDish + ", their favorite Surabaya delicacy.");
    }

    // Getter for favoriteDish
    public String getFavoriteDish() {
        return favoriteDish;
    }
}

// Main class to demonstrate usage
public class Main {
    public static void main(String[] args) {
        Javanese javaPerson = new Javanese("Adi", "Indonesia", "Batik Solo");
        javaPerson.eat();  // Output: Adi is enjoying a delicious Gudeg, their favorite food.
        javaPerson.dance();  // Output: Adi is performing a graceful Javanese dance.

        Banyumasan banyumasPerson = new Banyumasan("Budi", "Indonesia", "Batik Banyumas", "Intermediate");
        banyumasPerson.speakNgapak();  // Output: Budi is speaking with a Banyumasan accent (Ngapak).
        banyumasPerson.eat();  // Output: Budi is enjoying a delicious Gudeg, their favorite food.

        Surabayan surabayaPerson = new Surabayan("Citra", "Indonesia", "Batik Surabaya", "Rujak Cingur");
        surabayaPerson.eat();  // Output: Citra is enjoying a plate of Rujak Cingur, their favorite Surabaya delicacy.
        surabayaPerson.dance();  // Output: Citra is performing a graceful Javanese dance.

        Hakka hakkaPerson = new Hakka("Lin", "Indonesia", "Hakka");
        hakkaPerson.celebrateImlek();  // Output: Lin is celebrating Imlek with family and friends.
        hakkaPerson.celebrateHakkaCuisine();  // Output: Lin is savoring authentic Hakka cuisine.
        hakkaPerson.eat();  // Output: Lin is having Hakka-style dishes for dinner.
    }
}
