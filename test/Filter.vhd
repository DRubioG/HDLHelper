library IEEE;
use ieee.std_logic_1164.all;

entity Filter is
    generic(
        WIDTH : integer := 8;
        N_SAMPLES : integer := 124
    );
    port (
        clk : in std_logic;
        rst : in std_logic;
        en : in std_logic;
        clk_samples : in std_logic;
        sample : in std_logic_vector(WIDTH-1 downto 0);
        sample_ok : in std_logic;
        filter_out : out std_logic_vector(WIDTH-1 downto 0);
        filter_out_ok : out std_logic
    );
end entity;

architecture arch_Filter of Filter is
signal new_data : std_logic;
type filter_samples array (0 to N_SAMPLES-1) of std_logic_vector(WIDTH-1 downto 0);
constant filter_sample : filter_samples := ();
signal sample_init : std_logic_vector(WIDTH-1 downto 0);
signal values : 
begin

    process(clk, rst, en)
    begin
        if rst = '0' then

        elsif rising_edge(clk) then
            if en = '1' then
                if sample_ok = '1' then
                    sample_init <= sample;
                end if;
                -- if clk_sample = '1' then

                --     for i in 0 to N_SAMPLES loop

                --     end loop;
                -- else

                -- end if;
            elsif en = '0' then    

            end if;
        end if; 
    end process;

    -- generate_filter : for i in 0 to N_SAMPLES-1 generate


    -- end generate;


end architecture;