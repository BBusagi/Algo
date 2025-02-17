using System.Diagnostics;
using System.Linq;

/// <summary>
/// hashset 执行检索和存储
/// </summary>
public class Solution
{
    static void Main()
    {
        var nums = new int[]{1,1,2};
        RemoveDuplicates(nums);
    }

    static int RemoveDuplicates(int[] nums)
    {
        int index = 0;
        int index2 = 0;
        int[] newArray = new int[nums.Length];
        // foreach (var num in nums)
        // {
        //     Console.Write(num+" ");
        //     if (!newArray.Contains(num))
        //     {
        //         newArray[index2] = num;
        //         index2 ++;
        //     }
        //     index++;
        // }


        foreach(var n in newArray)
        {
            Console.Write(n);
        }
        return newArray.Length;
    }
}