namespace Math
{
	public class Calculator
	{
		public static int Factorial(int number)
		{
			int i;
			int fact = 1;
			for (i = 1; i <= number; i++)
			{
				fact *= i;
			}
			return fact;
		}
	}
}
