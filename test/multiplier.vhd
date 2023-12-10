library ieee;
use ieee.std_logic_164.all;
use ieee.numeric_std.all;

entity mult5 is
    port (
        clk, reset : in std_logic;
        a, b : in std_logic_vector(4 downto 0);
        y : out std_logic_vector(9 downto 0)
    );
end entity;

architecture comb_arch of mult5 is
    constant WIDTH : integer := 5;
    signal a0, a1, a2, a3 : std_logic_vector(WIDTH-1 downto 0);
    signal b0, b1, b2, b3 : std_logic_vector(WIDTH-1 downto 0);
    signal bv0, bv1, bv2, bv3, bv4 : std_logic_vector(WIDTH-1 downto 0);
    signal bp0, bp1, bp2, bp3, bp4 : unsigned(2*WIDTH-1 downto 0);
    signal pp0, pp1, pp2, pp3, pp4 : unsigned(2*WIDTH-1 downto 0);
begin
    -- stage 0
    bv0 <= (others=>b(0));
    bp0 <= unsigned("00000" & (bv0 and a));
    pp0 <= bp0;
    a0 <= a;
    b0 <= b;
    -- stage 1
    bv1 <= (others=>b0(1));
    bp1 <= unsigned("0000" & (bv1 and a0) & "0");
    pp1 <= pp0 + bp1;
    a1 <= a0;
    b1 <= b0;
    -- stage 2 
    bv2 <= (others=>b1(2));
    bp2 <= unsigned("00" & (bv2 and a1) & "00");
    pp2 <= pp1 + bp2;
    a2 <= a1;
    b2 <= b1;
    -- stage 3 
    bv3 <= (others=>b2(3));
    bp3 <= unsigned("00"&(bv3 and a2) & "000");
    pp3 <= pp2 + bp3;
    a3 <= a2;
    b3 <= b2;
    -- stage 4
    bv4 <= (others=>b3(4));
    bp4 <= unsigned("0" & (bv4 and a3) & "0000");
    pp4 <= pp3 + bp4;
    -- output
    y <= std_logic_vector(pp4);

end architecture;