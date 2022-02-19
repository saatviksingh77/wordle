import java.util.Scanner;
public class javaWordle
{
    public static void main()
    {
        Scanner sc = new Scanner(System.in);
        String answer="BOOKS";
        String guess;
        boolean correct=false;
        System.out.println("you have 6 chances\n# correct position\n* wrong position\n- not present\n");
        for(int i=1;i<=6;i++)
        {
            System.out.println("\n\nEnter guess "+i);
            guess=sc.next().toUpperCase();
            if(guess.length()!=5){
                System.out.print("Enter 5 letter string");
                i--;
            }
            else{
                for(int j=0;j<5;j++)
                {
                    if(guess.equals(answer)){
                        System.out.println("Correct");
                        correct=true;
                        break;
                    }
                    else if(guess.charAt(j)==answer.charAt(j))
                        System.out.print("#");
                    else if(answer.indexOf(guess.charAt(j))>=0 && answer.indexOf(guess.charAt(j))<5)
                        System.out.print("*");
                    else
                        System.out.print("-");
                }
            }
            if(correct)
                break;
            if(i==6)
                System.out.println("\nAll chances over, try again");
        }
    }
}
