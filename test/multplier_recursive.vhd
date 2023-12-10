----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 11/26/2023 06:48:21 PM
-- Design Name: 
-- Module Name: multplier_recursive - Behavioral
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

entity multplier_recursive is
    generic (
        WIDTH : integer := 5
    );
    Port ( 
        clk : in std_logic;
        rst : in std_logic;
        en  : in std_logic;
        start : in std_logic;
        finish : out std_logic;
        a : in std_logic_vector(WIDTH-1 downto 0);
        b : in std_logic_vector(WIDTH-1 downto 0);
        y : out std_logic_vector(2*WIDTH-1 downto 0)
    );
end multplier_recursive;

architecture Behavioral of multplier_recursive is
type fsm is (IDLE, READY, EXE, FIN);
signal state : fsm;

signal product, multiplicand : unsigned(2*WIDTH-1 downto 0);
signal multiplier : unsigned(WIDTH-1 downto 0);
signal cont : integer range 0 to WIDTH-1;
signal end_exe : std_logic;

begin
    process(rst, clk, end_exe)
    begin
        if rst = '1' then
            state <= IDLE;
        elsif rising_edge(clk) then
            if en = '1' then
                case state is
                    when IDLE =>
                        if start = '1' then
                            state <= READY;
                        end if;
                    when READY =>
                        state <= EXE;
                    when EXE =>
                        if end_exe = '1' then
                            state <= FIN;
                        end if;
                    when FIN =>
                        state <= IDLE;
                    when others =>
                end case;
            elsif en = '0' then
                state <= IDLE;
            end if;
        end if;        
    end process;


    process(rst, state)
    begin
        if rst = '1' then
            finish <= '0';
        else
            if en = '1' then
                case state is
                    when IDLE =>
                        finish <= '0';
                    when EXE =>
                        finish <= '0';
                    when FIN =>
                        finish <= '1';
                    when others =>
                        finish <= '0';
                end case;
            elsif en = '0' then
                finish <= '0';
            end if;
        end if;
    end process;

    process(clk,rst, en, state)
    
    begin
        if rst='1' then
            multiplicand <= (others=> '0');
            product <= (others=>'0');
            multiplier <= (others=>'0');
            end_exe <= '0';
            cont <= 0;
        elsif rising_edge(clk) then
            if en = '1' then
                case state is
                    when READY =>
                        multiplicand <= multiplicand + unsigned(b);
                        multiplier <= unsigned(a);
                        cont <= 0;
                    when EXE =>
                        if multiplier(0) = '1' then
                            product <= product+multiplicand;
                        end if;
                        multiplier <= "0" & multiplier(WIDTH-1 downto 1);
                        multiplicand <= multiplicand(2*WIDTH-2 downto 0) & "0";
                        if cont = WIDTH-1 then
                            cont <= 0;
                            end_exe <= '1';
                        else
                            cont <= cont+1;
                            end_exe <= '0';
                        end if;
                    when others => 
                        end_exe <= '0';
                        cont <= 0;
                end case;
            elsif en = '0' then
                multiplicand <= (others=> '0');
                product <= (others=>'0');
                multiplier <= (others=>'0');
                cont <= 0;
                end_exe <= '0';
            end if;
        end if;
    end process;

    
    y <= std_logic_vector(product);

end Behavioral;
