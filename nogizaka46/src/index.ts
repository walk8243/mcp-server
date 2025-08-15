import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { getMembersByGeneration, Nogizaka46Member } from "./data/members.js";

// Create server instance
const server = new McpServer({
	name: "nogizaka46",
	version: "1.0.0",
	capabilities: {
		resources: {},
		tools: {},
	},
});

// Register nogizaka46 tools
server.tool(
	"get_members",
	"Get members of a generation",
	{
		generation: z.number().positive().describe("Generation of the member"),
	},
	async ({ generation }) => {
		if (!generation) {
			return {
				content: [
					{
						type: "text",
						text: `Failed to get generation`,
					},
				],
			};
		}

		// Format Text
		const formattedText = getMembersByGeneration(generation).map((member: Nogizaka46Member) =>
			[
				`${member.name || "Unknown"}:`,
				`Name Kana: ${member.nameKana || "Unknown"}`,
				`Name English: ${member.nameEnglish || "Unknown"}`,
				`Birth Date: ${member.birthDate || "Unknown"}`,
				`Birth Place: ${member.birthPlace || "Unknown"}`,
				`Height: ${member.height || "Unknown"}`,
				`Blood Type: ${member.bloodType || "Unknown"}`,
				`Generation: ${member.generation}`,
				`Status: ${member.status || "Unknown"}`,
				`Join Date: ${member.joinDate || "Unknown"}`,
				`Description: ${member.description || "Unknown"}`,
			].join("\n"),
		);

		return {
			content: formattedText.map((text) => ({
				type: "text",
				text,
			})),
		};
	},
);

async function main() {
	const transport = new StdioServerTransport();
	await server.connect(transport);
	console.error("Nogizaka46 MCP Server running on stdio");
}

main().catch((error) => {
	console.error("Fatal error in main():", error);
	process.exit(1);
});
