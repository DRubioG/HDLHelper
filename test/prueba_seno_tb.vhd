----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/13/2023 04:49:59 PM
-- Design Name: 
-- Module Name: prueba_seno_tb - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity prueba_seno_tb is
--  Port ( );
end prueba_seno_tb;

architecture Behavioral of prueba_seno_tb is
component prueba_seno is
    generic(
            WIDTH : integer := 12;
            N : integer := 100
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        chirp : out std_logic_vector(WIDTH-1 downto 0);
        sine : out std_logic_vector(WIDTH-1 downto 0)
    );
end component;
constant WIDTH : integer := 12;
constant N : integer := 100;
signal clk : std_logic:='0';
signal rst : std_logic;
signal chirp, sine : std_logic_vector(WIDTH-1 downto 0);

begin
DUT : prueba_seno
    generic map (
            WIDTH => WIDTH,
            N => N
    )
    port map (
        clk => clk,
        rst => rst,
        chirp => chirp,
        sine => sine
    );

    clk <= not clk after 5ns;
    rst <= '1', '0' after 30ns;
    
    
end Behavioral;
