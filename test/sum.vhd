library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity sum_3 is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        input0 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        input1 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        input2 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        output : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end entity;

architecture arch_sum of sum_3 is

type fsm is (S0, EXE0, EXE1, FINISH);
signal state : fsm;

type inputs is array (2 downto 0) of std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
signal input : inputs;
signal cont : integer range 0 to 2;
signal sum_aux0 : unsigned(WIDTH_INT+WIDTH_DEC downto 0);
signal sum_aux1 : unsigned(WIDTH_INT+WIDTH_DEC+1 downto 0);

begin

    process(clk, rst, en)
    begin
        if rst = '0' then
            state <= S0;
        elsif rising_edge(clk) then
            if en = '1' then
                case state is
                    when S0 => 
                        if start = '1' then
                            state <= EXE;
                        else
                            state <= S0;
                        end if;
                    when EXE0 =>
                        state <= EXE1;
                    when EXE1 =>
                        state <= FINISH;
                    when FINISH =>
                        state <= S0;
                    when others =>
                        state <= S0;
                end case;
            elsif en = '0' then
                state <= S0;
            end if;
        end if;
    end process;

    process(rst, state)
    begin
        if rst = '0' then
            for i in 0 to 2 loop
                input(i) <= (others=>'0');
            end loop;
            sum_aux0 <= (others=>'0');
            sum_aux1 <= (others=>'0');
            finish <= '0';
        else
            case state is
                when S0 =>
                    finish <= '0';
                when EXE0 =>
                    sum_aux0 <= unsigned(input0) + unsigned(input1);
                when EXE1 =>
                    sum_aux1 <= sum_aux0 + unsigned(input2);
                when FINISH =>
                    finish <= '1';
                when others =>
                    output <= (others=>'0');
            end case;
        end if;
    end process;

    output <= sum_aux1(WIDTH_INT+WIDTH_DEC-1 downto 0);

end architecture;