export interface RecentXml {
	id: string;
	name: string;
	content: string;
}

export async function fetchRecentXml(count: number): Promise<RecentXml[]> {
	const response = await fetch(`/api/recent-xml?count=${count}`);
	if (!response.ok) return [];
	return response.json();
}