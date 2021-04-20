using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;
using System.Collections.Generic;


namespace ShipManagement
{
    class Program
    {
        static void Main(string[] args)
        {
            // Port workPort;
            // List<Port> = new List<Port>();
            //цикълът е направен, за да може при нужда да се завърти толкова пъти, 
            //че да вземе данните за всички пристанища налични в сайта
            //цикълът ще спре да се върти, когато се въведе опция различна от 1, 2 или 3 
            for(;;)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("-_-_-_-_-_-_-_-");
                //Activity selector
                Console.ResetColor();
                Console.WriteLine("Select the activity(by entering the number from the menu): ");
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine("1.Enter another port.");
                Console.WriteLine("2.Show port register.");
                Console.WriteLine("3.Clear the register.");
                Console.WriteLine("4.Exit.");
                Console.ResetColor();
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Available port numbers: 1, 3 - 20231 (not all numbers are real ports)");
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("-_-_-_-_-_-_-_-");
                Console.ResetColor();
                Console.ResetColor();
                //string се използва, за да не използваме обработка на exceptions
                string nextAc = Console.ReadLine();
                //Activity selector end
                //Tук се проверява оипцията, като се изрязват спейсовете на инпута
                switch(nextAc.Trim())
                {
                    //при опция едно ще извиква scraper-a, който също ще пише във файла
                    case "1": 
                        Scrape();
                            break;
                    //При опция 2 ще показва регистъра в конзолата
                    case "2": 
                        PrintRegister();
                            break;
                    //при опция 3 ще се чисти .txt файла
                    case "3": 
                        ClearRegister();
                            break;
                    //При различна опция ще излиза от програмата с код 0(успешно завършен)
                    default: 
                        Environment.Exit(0); 
                            break;
                }
            }
        }

        //тук просто се чете файла и се принтва
        public static void PrintRegister()
        {
            Console.ForegroundColor = ConsoleColor.Green;
            string register = File.ReadAllText("pD.txt");
            Console.WriteLine(register);
            Console.ResetColor();
        }
        //тук се чисти файла и се оставя определеният разделител
        public static void ClearRegister()
        {
            using (StreamWriter writer = new StreamWriter("pD.txt"))
            {
                writer.WriteLine("~~~~");
            }
        }
        // Тук извикваме скрипта, който ще scrape-ва страницата
        public static void Scrape()
        {
            OperatingSystem os = Environment.OSVersion;
            //Пита за номер на пристанище който скрипта си го чете
            Console.Write("Enter port number: ");
            //започва приготовлението, обработката и изпълнението на процеса около скрипта
            ProcessStartInfo start = new ProcessStartInfo();
            if (os.Platform.ToString() == "Unix")
            {
                start.FileName = "python3";
                start.Arguments = string.Format("Scraper.py Terminal");
            }
            else 
            {
                start.FileName = "python3.9.exe";
                start.Arguments = string.Format("Scraper.py cmd.exe");
            }
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using(Process process = Process.Start(start))
            {
                using(StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                }
            }
            //тук стигаме след изпълнение на скрипта
        }
    }
}
