Server=tcp:michaelwiciakserver.database.windows.net,1433;Initial Catalog=CW2;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;Authentication="Active Directory Default";

ado.net thing

The command to create table
CREATE TABLE data (
    [Id] UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
    [SensorId] INT NOT NULL,
    [Temperature] INT NOT NULL,
    [Wind] INT NOT NULL,
    [R.Humidity] INT NOT NULL,
    [CO2] INT NOT NULL
);

