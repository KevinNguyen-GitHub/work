using System;
using System.Collections.Generic;
using System.Linq;

namespace GenericSort
{
    class Program
    {
        static void Main(string[] args)
        {
            // Initializing the floating-point numbers array
            double[] floatInputs = { 645.41, 37.59, 76.41, 5.31, -34.23, 1.11,
                                     1.10, 23.46, 635.47, -876.32, 467.83, 62.25 };

            // Sorting the floating-point numbers array and printing it
            Console.WriteLine("Sorted Numbers in ascending order");
            SortAndPrint(floatInputs, (a, b) => a.CompareTo(b));

            // Initializing the dictionary of people
            Dictionary<string, int> names = new Dictionary<string, int>
            {
                {"Hal", 20},       {"Susann", 31},   {"Dwight", 19},
                {"Kassandra", 21}, {"Lawrence", 25}, {"Cindy", 22},
                {"Cory", 27},      {"Mac", 19},      {"Romana", 27},
                {"Doretha", 32},   {"Danna", 20},    {"Zara", 23},
                {"Rosalyn", 26},   {"Risa", 24},     {"Benny", 28},
                {"Juan", 33},      {"Natalie", 25}
            };

            // Sorting people alphabetically by name and printing
            Console.WriteLine("Mapped Names sorted by name");
            SortAndPrint(names, (a, b) => a.Key.CompareTo(b.Key));

            // Sorting people descending by age, then alphabetically by name, and printing
            Console.WriteLine("Mapped Names sorted by age descending, then by name");
            SortAndPrint(names, (a, b) => b.Value != a.Value ? b.Value.CompareTo(a.Value) : a.Key.CompareTo(b.Key));
        }

        static void SortAndPrint<T>(IEnumerable<T> collection, Comparison<T> comparison)
        {
            List<T> sortedList = collection.ToList();
            sortedList.Sort(comparison);

            foreach (T item in sortedList)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine();
        }
    }
}
