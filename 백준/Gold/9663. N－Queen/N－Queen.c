#include <stdio.h>

int	check(int row, int column, int	*arr)
{
	int	left_d;
	int	middle;
	int	right_d;
	int	std;

	left_d = column - 1;
	middle = column;
	right_d = column + 1;
	std = row - 1;
	while (0 <= std)
	{
		if (arr[std] == left_d || arr[std] == middle || arr[std] == right_d)
			return (0);
		std--;
		left_d--;
		right_d++;
	}
	return (1);
}

void	recursive(int *arr, char *ans, int row, int *cnt, int n)
{
	int	i;

	i = 0;
	if (row == n)
	{
		(*cnt)++;
		return ;
	}
	while (i < n)
	{
		arr[row] = i;
		if (check(row, i, arr))
			recursive(arr, ans, row + 1, cnt, n);
		i++;
	}
}

int	ft_ten_queens_puzzle(int n)
{
	int		cnt[1];
	int		arr[15];
	char	ans[15];

	recursive(arr, ans, 0, cnt, n);
	return (*cnt);
}

int    main(void)
{
    int    n;
    
    scanf("%d", &n);
    printf("%d", ft_ten_queens_puzzle(n));
}