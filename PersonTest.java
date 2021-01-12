import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.*;

class PersonTest {
    private int dudInstance = 1;
    @BeforeEach
    void setup() {
      assertTrue(true);
    }

    void dudMethod() {
      assertTrue(true);
    }

    @Test
    void Person() {
        dudMethod();
        assertEquals(1, dudInstance);
        Person p = new Person("Kevin", Person.Gender.MALE, 22);
        assertEquals(22, p.getAge(), "Age was wrong.");
        p.setAge(23);
        assertEquals(23, p.getAge(), "Age was wrong.");
        assertEquals("Kevin", p.getName(), "Name was wrong.");
    }

    @Test
    void Programmer() {
        dudMethod();
        assertEquals(1, dudInstance);
        Programmer p = new Programmer("Kevin", Person.Gender.MALE, 22);
        assertEquals(22, p.getAge(), "Age is incorrect.");
        assertEquals("Java", p.getFavoriteLanguage(), "Language is incorrect.");
        p.setFavoriteLanguage("Python");
        assertEquals("Python", p.getFavoriteLanguage(), "Language is incorrect.");
    }
}
