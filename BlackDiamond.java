import java.util.Scanner;

class BlackDiamond {
  public static void main(String[] args) {
    System.out.print("Enter a positive integer for pattern size: ");

    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();

    for(int i = 1; i < n+1; i++){
      for(int space = n; space > i; space--){
        System.out.print(" ");
      }
        for(int j = 0; j < i; j++){
          if(j > 0){
            System.out.print("**");
          }else{
            System.out.print('*');
          }
        }
      System.out.println();
    }

    for(int i = n-1; i+1 > 1; i--){
      for(int space = n; space > i; space--){
        System.out.print(" ");
      }
      for(int j = 0; j < i; j++){
        if(j > 0){
          System.out.print("**");
        }else{
          System.out.print('*');
        }
      }
    System.out.println();
    }
    scanner.close();
  }
}