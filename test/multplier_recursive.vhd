library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity multiplier_recursive is
    generic (
        WIDTH : integer := 5;
        DECIMAL : integer := 3
    );
    Port ( 
        clk : in std_logic;
        rst : in std_logic;
        en  : in std_logic;
        start : in std_logic;
        finish : out std_logic;
        a : in std_logic_vector(WIDTH-1 downto 0);
        b : in std_logic_vector(WIDTH-1 downto 0);
        y : out std_logic_vector(WIDTH-1 downto 0) --2*WIDTH-1 downto 0)
    );
end multiplier_recursive;


architecture Behavioral of multiplier_recursive is

type fsm is (IDLE, READY, EXE, FIN);
signal state : fsm;

signal product, multiplicand : unsigned(2*WIDTH-1 downto 0);
signal y_aux :  std_logic_vector(2*WIDTH-1 downto 0);
signal multiplier : unsigned(WIDTH-1 downto 0);
signal cont : integer range 0 to WIDTH-1;
signal end_exe : std_logic;

begin

FSM_declaration : process(rst, clk, end_exe)
    begin
        if rst = '0' then
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
                        state <= READY;
                end case;
            elsif en = '0' then
                state <= IDLE;
            end if;
        end if;        
    end process;


FSM_signals : process(rst, state)
    begin
        if rst = '0' then
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


MULTIPLICATION : process(clk,rst, en, state)
    begin
        if rst='0' then
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

    
    y_aux <= std_logic_vector(product);
    y <= y_aux(WIDTH+(WIDTH-DECIMAL) downto DECIMAL);

end Behavioral;
