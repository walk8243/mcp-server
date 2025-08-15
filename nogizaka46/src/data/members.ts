export const nogizaka46Members: Nogizaka46Member[] = [
	{
		id: "1gen-1",
		name: "秋元真夏",
		nameKana: "あきもと まなつ",
		nameEnglish: "Akimoto Manatsu",
		birthDate: "1993-08-20",
		birthPlace: "東京都",
		height: 154,
		bloodType: "B",
		generation: 1,
		status: "active",
		joinDate: "2011-08-21",
		description: "乃木坂46のキャプテン。1期生としてグループを支える中心的存在。"
	},
	{
		id: "1gen-2",
		name: "生田絵梨花",
		nameKana: "いくた えりか",
		nameEnglish: "Ikuta Erika",
		birthDate: "1997-01-22",
		birthPlace: "東京都",
		height: 160,
		bloodType: "A",
		generation: 1,
		status: "graduated",
		joinDate: "2011-08-21",
		graduationDate: "2021-12-31",
		description: "ピアニストとしても活躍。グループの音楽面での中心的存在だった。"
	},
	{
		id: "1gen-3",
		name: "白石麻衣",
		nameKana: "しらいし まい",
		nameEnglish: "Shiraishi Mai",
		birthDate: "1992-08-20",
		birthPlace: "群馬県",
		height: 162,
		bloodType: "A",
		generation: 1,
		status: "graduated",
		joinDate: "2011-08-21",
		graduationDate: "2020-10-28",
		description: "グループの顔として活躍。ファッション誌での活躍も目立った。"
	},
	{
		id: "2gen-1",
		name: "新内眞衣",
		nameKana: "しんうち まい",
		nameEnglish: "Shinuchi Mai",
		birthDate: "1992-01-22",
		birthPlace: "東京都",
		height: 162,
		bloodType: "A",
		generation: 2,
		status: "graduated",
		joinDate: "2013-03-28",
		graduationDate: "2021-12-31",
		description: "2期生としてグループを支えた。"
	},
	{
		id: "3gen-1",
		name: "大園桃子",
		nameKana: "おおぞの ももこ",
		nameEnglish: "Oozono Momoko",
		birthDate: "2002-04-28",
		birthPlace: "鹿児島県",
		height: 158,
		bloodType: "O",
		generation: 3,
		status: "graduated",
		joinDate: "2016-09-04",
		graduationDate: "2021-09-04",
		description: "3期生として活躍。"
	},
	{
		id: "4gen-1",
		name: "遠藤さくら",
		nameKana: "えんどう さくら",
		nameEnglish: "Endo Sakura",
		birthDate: "2001-10-03",
		birthPlace: "愛知県",
		height: 163,
		bloodType: "A",
		generation: 4,
		status: "active",
		joinDate: "2018-11-30",
		description: "4期生の中心的存在。グループの次世代を担う。"
	},
	{
		id: "4gen-2",
		name: "賀喜遥香",
		nameKana: "かき はるか",
		nameEnglish: "Kaki Haruka",
		birthDate: "2001-08-17",
		birthPlace: "栃木県",
		height: 160,
		bloodType: "A",
		generation: 4,
		status: "active",
		joinDate: "2018-11-30",
		description: "4期生として活躍。グループの中心メンバー。"
	},
	{
		id: "5gen-1",
		name: "池田瑛紗",
		nameKana: "いけだ てるさ",
		nameEnglish: "Ikeda Terusa",
		birthDate: "2002-05-12",
		birthPlace: "東京都",
		height: 158,
		bloodType: "A",
		generation: 5,
		status: "active",
		joinDate: "2022-02-01",
		description: "5期生として新たにグループに加わった。"
	},
	{
		id: "5gen-2",
		name: "一ノ瀬美空",
		nameKana: "いちのせ みそら",
		nameEnglish: "Ichinose Misora",
		birthDate: "2004-05-02",
		birthPlace: "神奈川県",
		height: 160,
		bloodType: "O",
		generation: 5,
		status: "active",
		joinDate: "2022-02-01",
		description: "5期生の最年少メンバー。"
	}
];

export const getActiveMembers = (): Nogizaka46Member[] => {
	return nogizaka46Members.filter(member => member.status === 'active');
};

export const getMembersByGeneration = (generation: number): Nogizaka46Member[] => {
	return nogizaka46Members.filter(member => member.generation === generation);
};

export const getMemberById = (id: string): Nogizaka46Member | undefined => {
	return nogizaka46Members.find(member => member.id === id);
};

export interface Nogizaka46Member {
	id: string;
	name: string;
	nameKana: string;
	nameEnglish: string;
	birthDate: string;
	birthPlace: string;
	height: number;
	bloodType: string;
	generation: number;
	status: 'active' | 'graduated' | 'suspended';
	joinDate: string;
	graduationDate?: string;
	imageUrl?: string;
	description?: string;
}

export interface MemberListResponse {
	members: Nogizaka46Member[];
	totalCount: number;
	lastUpdated: string;
}
