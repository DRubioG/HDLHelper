library ieee;
use ieee.std_logic_1164.all;

entity matrix_coef_3 is
    generic(
        WIDTH_INT : integer := 10;
        WIDTH_DEC : integer := 8
    );
    port(
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        a0, a1, a2, b0, b1, b2 : in std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
        start : in std_logic;
        finish : out std_logic;
        output : out std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0)
    );
end entity;


architecture arch_matrix_coef_3 of matrix_coef_3 is

component multiplier_recursive is
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
end component;

component sum_3 is
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
end component;

signal result_mul0, result_mul1, result_mul2 : std_logic_vector(WIDTH_INT+WIDTH_DEC-1 downto 0);
signal finish_mul0, finish_mul1, finish_mul2 : std_logic;
signal finish_and : std_logic;

begin

MUL0 : multiplier_recursive
    generic map(
        WIDTH => 
    )
    Port map ( 
        clk => clk,
        rst => rst,
        en  => en,
        start => start,
        finish => finish_mul0,
        a => a0,
        b => b0,
        y => result_mul0
    );

MUL1 : multiplier_recursive
    generic map (
        WIDTH => 
    )
    Port map( 
        clk => clk,
        rst => rst,
        en  => en,
        start => start,
        finish => finish_mul1,
        a => a1,
        b => b1,
        y => result_mul1
    );

MUL2 : multiplier_recursive
    generic map(
        WIDTH => 
    )
    Port map( 
        clk => clk,
        rst => rst,
        en  => en,
        start => start,
        finish => finish_mul2
        a => a2,
        b => b2,
        y => result_mul2
    );

    finish_and <= finish_mul0 and finish_mul1 and finish_mul2;

SUM : sum_3
    generic map(
        WIDTH_INT => WIDTH_INT,
        WIDTH_DEC => WIDTH_DEC
    )
    port map(
        clk => clk,
        rst => rst,
        en => en,
        input0 => result_mul0,
        input1 => result_mul1,
        input2 => result_mul2,
        start => finish_and,
        finish => finish,
        output => output
    );

end architecture;