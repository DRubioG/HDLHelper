entity prueba is
	port(clk : in std_logic)
end entity prueba;

architecture arch_prueba of prueba is

component prueba is
	generic (
		yfg6yugiukj	 : 	integer;
		U          	 : 	integer          := 	32;
		N          	 : 	integer;
		T          	 : 	integer;
		Gad        	 : 	std_logic_vector := 	N-1
	);
	port (
		clk                  	 : 	in  std_logic;
		rst                  	 : 	in  std_logic;
		yhmm                 	 : 	in  std_logic;
		Rowerererrererererere	 : 	in  std_logic_vector((N-1) downto (N-2));
		Col                  	 : 	out std_logic_vector(3 downto 0);
		DecodeOut            	 : 	out std_logic_vector(3 downto 0));
end component;

constant yfg6yugiukj : integer;
constant U           : integer	 := 32;
constant N           : integer;
constant T           : integer;
constant Gad         : std_logic_vector	 := N-1;

constant yfg6yugiukj : integer;
constant U           : integer	 := 32;
constant N           : integer;
constant T           : integer;
constant Gad         : std_logic_vector	 := N-1;

signal clk                   : std_logic;
signal rst                   : std_logic;
signal yhmm                  : std_logic;
signal Rowerererrererererere : std_logic_vector((N-1) downto (N-2));
signal Col                   : std_logic_vector(3 downto 0);
signal DecodeOut             : std_logic_vector(3 downto 0);

signal clk                   : std_logic;
signal rst                   : std_logic;
signal yhmm                  : std_logic;
signal Rowerererrererererere : std_logic_vector((N-1) downto (N-2));
signal Col                   : std_logic_vector(3 downto 0);
signal DecodeOut             : std_logic_vector(3 downto 0);


begin

pru_inst : prueba
	generic map (
		yfg6yugiukj	 => 	yfg6yugiukj,
		U          	 => 	U,
		N          	 => 	N,
		T          	 => 	T,
		Gad        	 => 	Gad
	)
	port map (
		clk                  	 => 	clk,
		rst                  	 => 	rst,
		yhmm                 	 => 	yhmm,
		Rowerererrererererere	 => 	Rowerererrererererere,
		Col                  	 => 	Col,
		DecodeOut            	 => 	DecodeOut,
	);

pru_inst : prueba
	generic map (
		yfg6yugiukj	 => 	yfg6yugiukj,
		U          	 => 	U,
		N          	 => 	N,
		T          	 => 	T,
		Gad        	 => 	Gad
	)
	port map (
		clk                  	 => 	clk,
		rst                  	 => 	rst,
		yhmm                 	 => 	yhmm,
		Rowerererrererererere	 => 	Rowerererrererererere,
		Col                  	 => 	Col,
		DecodeOut            	 => 	DecodeOut,
	);



end architecture arch_prueba;