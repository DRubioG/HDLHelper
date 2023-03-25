library IEEE;
use IEEE.std_logic_1164.all;
component miIP is
	generic (
		C_S00_AXI_DATA_WIDTH	 : integer := 	32;
		C_S00_AXI_ADDR_WIDTH	 : integer := 	4
	)
	port (
		s00_axi_aclk    	 : in 	std_logic;                                                            
		s00_axi_aresetn 	 : in 	std_logic;                                                            
		ss00_axi_awaddr 	 : in 	std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0);                    
		s00_axi_awprot  	 : in 	std_logic_vector(2 downto 0);                                         
		ss00_axi_awvalid	 : in 	std_logic;                                                            
		ss00_axi_awready	 : out	std_logic;                                                            
		s00_axi_wdata   	 : in 	std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0);                    
		s00_axi_wstrb   	 : in 	std_logic_vector(C_S00_AXI_DATA_WIDTH/8-1 downto 0);                  
		s00_axi_wvalid  	 : in 	std_logic;                                                            
		s00_axi_wready  	 : out	std_logic;                                                            
		s00_axi_bresp   	 : out	std_logic_vector(1 downto 0);                                         
		s00_axi_bvalid  	 : out	std_logic;                                                            
		s00_axi_bready  	 : in 	std_logic;                                                            
		s00_axi_araddr  	 : in 	std_logic_vector(C_S00_AXI_ADDR_WIDTH-1 downto 0);                    
		s00_axi_arprot  	 : in 	std_logic_vector(2 downto 0);                                         
		s00_axi_arvalid 	 : in 	std_logic;                                                            
		s00_axi_arready 	 : out	std_logic;                                                            
		s00_axi_rdata   	 : out	std_logic_vector(C_S00_AXI_DATA_WIDTH-1 downto 0);                    
		ss00_axi_rresp  	 : out	std_logic_vector(1 downto 0);                                         
		s00_axi_rvalid  	 : out	std_logic;                                                            
		s00_axi_rready  	 : in 	std_logic);                                                           
end component;
