library IEEE;
use ieee.std_logic_1164.all;

entity prueba_seno is
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
end entity;

architecture arch_prueba_seno of prueba_seno is
type seno_array is array (0 to N-1) of std_logic_vector(WIDTH-1 downto 0);
type chirp_array is array (0 to N-1) of std_logic_vector(WIDTH-1 downto 0);

signal seno : seno_array := (x"800", x"881", x"903", x"983", x"a02", x"a7f", x"af9", x"b70", x"be3", x"c53", x"cbe", x"d24", x"d85", x"de0", x"e35", x"e84", x"ecc", x"f0d", x"f46", x"f79", x"fa3", x"fc6", x"fe0", x"ff3", x"ffd", x"fff", x"ff9", x"feb", x"fd4", x"fb5", x"f8f", x"f60", x"f2a", x"eed", x"ea9", x"e5d", x"e0b", x"db3", x"d55", x"cf1", x"c89", x"c1c", x"baa", x"b35", x"abc", x"a40", x"9c3", x"943", x"8c2", x"840", x"7bf", x"73d", x"6bc", x"63c", x"5bf", x"543", x"4ca", x"455", x"3e3", x"376", x"30e", x"2aa", x"24c", x"1f4", x"1a2", x"156", x"112", x"0d5", x"09f", x"070", x"04a", x"02b", x"014", x"006", x"000", x"002", x"00c", x"01f", x"039", x"05c", x"086", x"0b9", x"0f2", x"133", x"17b", x"1ca", x"21f", x"27a", x"2db", x"341", x"3ac", x"41c", x"48f", x"506", x"580", x"5fd", x"67c", x"6fc", x"77e", x"7ff");

signal chirp_s : chirp_array := (x"999", x"ffb", x"fed", x"fd2", x"faa", x"f72", x"f29", x"ecd", x"e5c", x"dd6", x"d39", x"c86", x"bbc", x"add", x"9eb", x"8e8", x"7d8", x"6c0", x"5a5", x"48e", x"382", x"289", x"1ad", x"0f5", x"06b", x"017", x"000", x"02c", x"09d", x"155", x"252", x"38e", x"501", x"69c", x"850", x"a09", x"bb2", x"d33", x"e75", x"f62", x"fe7", x"ff7", x"f8a", x"ea0", x"d42", x"b82", x"97c", x"751", x"52a", x"333", x"197", x"07d", x"003", x"03b", x"128", x"2bd", x"4d9", x"74c", x"9d9", x"c3e", x"e37", x"f86", x"fff", x"f8c", x"e30", x"c0e", x"963", x"682", x"3cb", x"19c", x"04a", x"00c", x"0f4", x"2ea", x"5ab", x"8d1", x"bde", x"e52", x"fc1", x"fe3", x"ea8", x"c3c", x"907", x"599", x"296", x"096", x"003", x"108", x"379", x"6e1", x"a8d", x"db4", x"fa2", x"fe0", x"e53", x"b4a", x"775", x"3b8", x"100", x"000");

signal cont : integer range 0 to 2**WIDTH-1;
begin
    process(clk, rst)
--    variable cont : integer range 0 to 2**WIDTH-1;
    begin
        if rst = '1' then
            cont <= 0;
            sine <= (others=>'0');
            chirp <= (others=>'0');
        elsif rising_edge(clk) then
            sine <= seno(cont);
            chirp <= chirp_s(cont);
            if cont = N-1 then
                cont <= 0;
            else
                cont <= cont +1;
            end if;
        end if;
    end process;





end architecture;