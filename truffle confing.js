module.exports = {
  networks: {
    development: {
      host: "127.0.0.1", // Localhost (default: none)
      port: 7545,        // Portul implicit pe care rulează Ganache
      network_id: "*",   // Se potrivește cu orice ID de rețea (default: none)
    },
  },
  compilers: {
    solc: {
      version: "0.8.0", // Specifică versiunea compilatorului Solidity
    },
  },
};