library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier2 is
    generic (
        WIDTH : integer := 5
    );
    port (
        clk, reset : in std_logic;
        a, b : in unsigned(WIDTH-1 downto 0);
        y : out std_logic_vector(2*WIDTH-1 downto 0)
    );
end entity;

architecture tree_pipe_arch of multiplier2 is
    signal bv0, bv1, bv2, bv3, bv4 : unsigned(WIDTH-1 downto 0);
    signal bp0, bp1, bp2, bp3, bp4 : unsigned(2*WIDTH-1 downto 0);
    
    signal bp : is 
    
    signal bp4_s1_reg, bp4_s2_reg : unsigned(2*WIDTH-1 downto 0);
    signal bp4_s1_next, bp4_s2_next : unsigned(2*WIDTH-1 downto 0);
    signal pp01_reg, pp23_reg, pp0123_reg, pp01234_reg : unsigned(2*WIDTH-1 downto 0);
    signal pp01_next, pp23_next, pp0123_next, pp01234_next : unsigned(2*WIDTH-1 downto 0);
    
begin

    process(clk, reset)
    begin
        if reset = '1' then
            pp01_reg <= (others=>'0');
            pp23_reg <= (others=>'0');
            pp0123_reg <= (others=>'0');
            pp01234_reg <= (others=>'0');
            bp4_s1_reg <= (others=>'0');
            bp4_s2_reg <= (others=>'0');
        elsif rising_edge(clk) then
            pp01_reg <= pp01_next;
            pp23_reg <= pp23_next;
            pp0123_reg <= pp0123_next;
            pp01234_reg <= pp01234_next;
            bp4_s1_reg <= bp4_s1_next;
            bp4_s2_reg <= bp4_s2_next;
        end if;
    end process;
    -- stage 1
    -- bit product
    bv0 <= (others=>b(0));
    bp0 <= unsigned("00000" & (bv0 and a));
    
    bv1 <= (others=>b(1));
    bp1 <= unsigned("0000" & (bv1 and a) & "0");
    
    bv2 <= (others=>b(2));
    bp2 <= unsigned("000" & (bv2 and a) & "00");
    
    bv3 <= (others=>b(3));
    bp3 <= unsigned("00" & (bv3 and a) & "000");
    
    bv4 <= (others=>b(4));
    bp4 <= unsigned("0" & (bv4 and a) & "0000");
    
    -- adder
    pp01_next <= bp0 + bp1;
    pp23_next <= bp2 + bp3;
    bp4_s1_next <= bp4;
    -- stage 2
    pp0123_next <= pp01_reg + pp23_reg;
    bp4_s2_next <= bp4_s1_reg;
    -- stage 3
    pp01234_next <= pp0123_reg + bp4_s2_reg;
    -- output
    y <= std_logic_vector(pp01234_reg);


end architecture;