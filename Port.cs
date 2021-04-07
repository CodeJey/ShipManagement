namespace ShipManagement
{
    public class Port
    {
        internal string name, coordinates, unLcode, country;
        internal int portNumber, shipsCount;
        
        public Port(string name, string coordinates, string unLcode, string country, int portNumber, int shipsCount)
        {
            this.name = name;
            this.coordinates = coordinates;
            this.unLcode = unLcode;
            this.country = country;
            this.portNumber = portNumber;
            this.shipsCount = shipsCount;
        }
    }
}