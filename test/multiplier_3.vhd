----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/26/2023 05:39:04 PM
-- Design Name: 
-- Module Name: multiplier_3 - Behavioral
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
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity multiplier_3 is
    generic(
        WIDTH : integer := 3
    );
    Port ( 
        clk, rst : in std_logic;
        a, b : in unsigned(WIDTH-1 downto 0);
        y : out std_logic_vector(2*WIDTH-1 downto 0)
    );
end multiplier_3;

architecture Behavioral of multiplier_3 is
constant cero : unsigned(WIDTH-1 downto 0):= "000";
--constant hola : unsigned(WIDTH-1 downto 0);-- := (0, WIDTH);

type bp_matrix is array (WIDTH-1 downto 0) of unsigned(2*WIDTH-1 downto 0);
signal bp : bp_matrix;

type bv_matrix is array (WIDTH-1 downto 0) of unsigned(WIDTH-1 downto 0);
signal bv : bv_matrix;

begin

    process(rst, a, b)
    begin
        if rst = '1' then
            for i in 0 to WIDTH-1 loop
                bv(i) <= (others=>'0');
                bp(i) <= (others=>'0');
            end loop;
        else
            for i in 0 to WIDTH-1 loop
                bv(i) <= (others=>b(i));
                if i = 0 then
                    bp(i) <= (cero & (bv(i) and a));
                elsif i = WIDTH-1 then
                    bp(i) <= ("0" & (bv(i) and a) & cero(i-1 downto 0));
                else
                    bp(i) <= (cero(WIDTH-1 downto WIDTH-1-i) & (bv(i) and a) & cero(i-1 downto 0));
                end if;
            end loop;
        end if;
    end process;
    
    
    
    
    

end Behavioral;
